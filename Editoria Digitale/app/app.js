const express = require("express");
const app = express();
const PORT = 8080 || process.env.PORT;
const dotenv = require("dotenv");
const jwt = require("jsonwebtoken");
const bcrypt = require("bcrypt");
const path = require("path");
const User = require("./models/user");
const { default: mongoose } = require("mongoose");

dotenv.config({ path: "./.env" });
const publicDirectory = path.join(__dirname, "./public");
app.use(express.static(publicDirectory));
mongoose.set("strictQuery", false);
mongoose.connect(process.env.MONGOKEY, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

app.set("view engine", "hbs");

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get("/", (req, res) => {
  res.render("index");
});

app.get("/login", (req, res) => {
  if (req.headers.cookie) {
    let token = req.headers.cookie.split("=")[1];
    jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
      if (err) {
        res.render("login");
      } else {
        res.redirect("/dashboard");
      }
    });
  }
  res.render("login");
});

app.post("/login", async (req, res) => {
  try {
    const { email, password } = req.body;
    if (!email || !password) {
      return res.status(400).render("login", {
        message: "Please provide an email and password",
      });
    } else {
      const user = await User.findOne({ email }).lean();
      if (!user) {
        return res.status(400).render("login", {
          message: "Please provide an email and password",
        });
      } else {
        if (await bcrypt.compare(password, user.password)) {
          const token = jwt.sign(
            {
              id: user._id,
              name: user.name,
              email: user.email,
              refId: user.refId,
              questions: user.questions,
            },
            process.env.JWT_SECRET,
            {
              expiresIn: "1h",
            }
          );
          res.cookie("token", token, {
            httpOnly: true,
            maxAge: 1000 * 60 * 60,
          });
          return res.status(200).redirect("/dashboard");
        } else {
          return res.status(400).render("login", {
            message: "Please provide an email and password",
          });
        }
      }
    }
  } catch (err) {
    console.log(err);
  }
});

app.get("/register", (req, res) => {
  res.render("register");
});

app.post("/register", async (req, res) => {
  try {
    const { name, email, password, passwordConfirm } = req.body;
    if (!name || !email || !password || !passwordConfirm) {
      return res.status(400).render("register", {
        message: "Please provide an email and password",
      });
    } else if (password !== passwordConfirm) {
      return res.status(400).render("register", {
        message: "Passwords do not match",
      });
    } else {
      let user = await User.findOne({ email });
      if (user) {
        return res.status(400).render("register", {
          message: "That email is already in use",
        });
      }

      const questions = {
        chapter1: {
          name: "Chapter 1 - Sneaker Game",
          question:
            "What is the right mindset to have when you are starting out?",
          answer:
            "The right mindset is proactive with regards to risk. You should be willing to take risks and learn from your mistakes.",
          description:
            "An overview of the sneaker reselling industry, including its history and current state.",
          solved: false,
          chapter_id: 1,
        },
        chapter2: {
          name: "Chapter 2 - Markets",
          question: "In which market can the most expensive shoes be found?",
          answer:
            "The luxury shoe market, such as high-end department stores and designer boutiques, typically offers the most expensive shoes.",
          description:
            "An in-depth look at the various markets where sneakers can be bought and sold, including online marketplaces and local shops.",
          solved: false,
          chapter_id: 2,
        },
        chapter3: {
          name: "Chapter 3 - How to Buy",
          question:
            "What is the most important factor to consider when buying shoes?",
          answer:
            "It's also important to consider the current market price of the shoes before making a purchase to avoid overpaying.",
          description:
            "Tips and strategies for finding and purchasing sneakers to resell, including verifying authenticity and considering market prices.",
          solved: false,
          chapter_id: 3,
        },
        chapter4: {
          name: "Chapter 4 - How to Sell",
          question:
            "What is the most important factor to consider when selling shoes?",
          answer:
            "To increase the chances of selling a pair of shoes, it's important to provide detailed photographs and accurate descriptions of the shoes, and to use multiple selling platforms to reach a wider audience.",
          description:
            "Strategies for pricing and selling sneakers, including using multiple platforms and providing detailed descriptions and photographs.",
          solved: false,
          chapter_id: 4,
        },
      };
      const refId = Math.floor(Math.random() * 100000000000000000);
      const salt = await bcrypt.genSalt(10);
      const hashedPassword = await bcrypt.hash(password, salt);
      user = new User({
        name,
        email,
        password: hashedPassword,
        refId,
        questions,
      });
      await user.save();
      console.log(user);
      res.status(201).redirect("/login");
    }
  } catch (error) {
    if (error.code === 11000) {
      return res.status(400).render("register", {
        message: "That email is already in use",
      });
    }
  }
});

app.get("/dashboard", (req, res) => {
  let cookie = req.headers.cookie;
  let query = req.query;
  console.log(query);
  if (cookie) {
    let token = cookie.split("=")[1];
    jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
      if (err) {
        return res.redirect("/login");
      } else {
        decoded = jwt.decode(token);
        id = decoded.refId;
        name = decoded.name;

        User.find({ refId: id }, (err, user) => {
          if (err) {
            console.log(err);
          } else {
            console.log(user);
            name = user[0].name;
            questions = user[0].questions;
            description = user[0].description;
            res.render("dash", { name, id, questions, description });
          }
        });
      }
    });
  } else {
    return res.redirect("/login");
  }
});

app.post("/api/1/check", (req, res) => {
  const { answer } = req.body;
  console.log(answer);
  let cookie = req.headers.cookie;
  console.log(req.query);
  if (cookie) {
    let token = cookie.split("=")[1];
    jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
      if (err) {
        return res.redirect("/login");
      } else {
        decoded = jwt.decode(token);
        id = decoded.refId;
        User.find({ refId: id }, (err, user) => {
          if (err) {
            console.log(err);
          } else {
            user = user[0];
            name = user.name;
            questions = user.questions;
            question = questions.chapter1.question;
            if (answer == questions.chapter1.answer) {
              questions.chapter1.solved = true;
              User.findOneAndUpdate(
                { refId: id },
                { questions: questions },
                (err, doc) => {
                  if (err) {
                    console.log("Something wrong when updating data!");
                  }
                  console.log(doc, "updated");
                }
              );
              res.redirect("/dashboard?done=true");
            } else {
              res.redirect("/1/quiz");
            }
          }
        });
      }
    });
  }
});

app.post("/api/2/check", (req, res) => {
  const { answer } = req.body;
  let cookie = req.headers.cookie;
  console.log(req.query);
  if (cookie) {
    let token = cookie.split("=")[1];
    jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
      if (err) {
        return res.redirect("/login");
      } else {
        decoded = jwt.decode(token);
        id = decoded.refId;
        User.find({ refId: id }, (err, user) => {
          if (err) {
            console.log(err);
          } else {
            user = user[0];
            name = user.name;
            questions = user.questions;
            question = questions.chapter2.question;
            if (answer == questions.chapter2.answer) {
              questions.chapter2.solved = true;
              User.findOneAndUpdate(
                { refId: id },
                { questions: questions },
                (err, doc) => {
                  if (err) {
                    console.log("Something wrong when updating data!");
                  }
                  console.log(doc, "updated");
                }
              );
              res.redirect("/dashboard?done=true");
            } else {
              res.redirect("/2/quiz");
            }
          }
        });
      }
    });
  }
});

app.post("/api/3/check", (req, res) => {
  const { answer } = req.body;
  let cookie = req.headers.cookie;
  console.log(req.query);
  if (cookie) {
    let token = cookie.split("=")[1];
    jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
      if (err) {
        return res.redirect("/login");
      } else {
        decoded = jwt.decode(token);
        id = decoded.refId;
        User.find({ refId: id }, (err, user) => {
          if (err) {
            console.log(err);
          } else {
            user = user[0];
            name = user.name;
            questions = user.questions;
            question = questions.chapter3.question;
            if (answer == questions.chapter3.answer) {
              questions.chapter3.solved = true;
              User.findOneAndUpdate(
                { refId: id },
                { questions: questions },
                (err, doc) => {
                  if (err) {
                    console.log("Something wrong when updating data!");
                  }
                  console.log(doc, "updated");
                }
              );
              res.redirect("/dashboard?done=true");
            } else {
              res.redirect("/3/quiz");
            }
          }
        });
      }
    });
  }
});

app.post("/api/4/check", (req, res) => {
  const { answer } = req.body;
  let cookie = req.headers.cookie;
  console.log(req.query);
  if (cookie) {
    let token = cookie.split("=")[1];
    jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
      if (err) {
        return res.redirect("/login");
      } else {
        decoded = jwt.decode(token);
        id = decoded.refId;
        User.find({ refId: id }, (err, user) => {
          if (err) {
            console.log(err);
          } else {
            user = user[0];
            name = user.name;
            questions = user.questions;
            question = questions.chapter4.question;
            if (answer == questions.chapter4.answer) {
              questions.chapter4.solved = true;
              User.findOneAndUpdate(
                { refId: id },
                { questions: questions },
                (err, doc) => {
                  if (err) {
                    console.log("Something wrong when updating data!");
                  }
                  console.log(doc, "updated");
                }
              );
              res.redirect("/dashboard?done=true");
            } else {
              res.redirect("/4/quiz");
            }
          }
        });
      }
    });
  }
});

app.get("/1/quiz", (req, res) => {
  let cookie = req.headers.cookie;
  console.log(req.query);
  if (cookie) {
    let token = cookie.split("=")[1];
    jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
      if (err) {
        return res.redirect("/login");
      } else {
        decoded = jwt.decode(token);
        id = decoded.refId;
        name = decoded.name;
        questions = decoded.questions;
        question = questions.chapter1.question;
        answer = questions.chapter1.answer;
        console.log("thats", question);
        res.render("quiz1", { name, id, question, answer });
      }
    });
  } else {
    return res.redirect("/login");
  }
});

app.get("/2/quiz", (req, res) => {
  let cookie = req.headers.cookie;
  console.log(req.query);
  if (cookie) {
    let token = cookie.split("=")[1];
    jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
      if (err) {
        return res.redirect("/login");
      } else {
        decoded = jwt.decode(token);
        id = decoded.refId;
        name = decoded.name;
        questions = decoded.questions;
        question = questions.chapter2.question;
        answer = questions.chapter2.answer;
        console.log("thats", question);
        res.render("quiz2", { name, id, question, answer });
      }
    });
  } else {
    return res.redirect("/login");
  }
});

app.get("/3/quiz", (req, res) => {
  let cookie = req.headers.cookie;
  console.log(req.query);
  if (cookie) {
    let token = cookie.split("=")[1];
    jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
      if (err) {
        return res.redirect("/login");
      } else {
        decoded = jwt.decode(token);
        id = decoded.refId;
        name = decoded.name;
        questions = decoded.questions;
        question = questions.chapter3.question;
        answer = questions.chapter3.answer;
        console.log("thats", question);
        res.render("quiz3", { name, id, question, answer });
      }
    });
  } else {
    return res.redirect("/login");
  }
});

app.get("/4/quiz", (req, res) => {
  let cookie = req.headers.cookie;
  console.log(req.query);
  if (cookie) {
    let token = cookie.split("=")[1];
    jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
      if (err) {
        return res.redirect("/login");
      } else {
        decoded = jwt.decode(token);
        id = decoded.refId;
        name = decoded.name;
        questions = decoded.questions;
        question = questions.chapter4.question;
        answer = questions.chapter4.answer;
        console.log("thats", question);
        res.render("quiz4", { name, id, question, answer });
      }
    });
  } else {
    return res.redirect("/login");
  }
});

app.get("/logout", (req, res) => {
  res.clearCookie("token");
  res.redirect("/login");
});

app.get("/404", (req, res) => {
  res.render("404");
});

app.get("/:id", (req, res) => {
  let listEndpoints = [
    "login",
    "register",
    "dashboard",
    "logout",
    "1/quiz",
    "2/quiz",
    "3/quiz",
    "4/quiz",
  ];
  if (listEndpoints.includes(req.params.id) == false) {
    res.redirect("/404");
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on port http://localhost:${PORT}/`);
});
