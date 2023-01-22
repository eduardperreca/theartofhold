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
          name: "chapter 1 - functions",
          question: "What is the difference between a variable and a constant?",
          answer: "A variable can be changed, a constant cannot.",
          solved: false,
          chapter_id: 1,
        },
        chapter2: {
          name: "chapter 2 - functions",
          question: "What is the difference between a variable and a constant?",
          answer: "A variable can be changed, a constant cannot.",
          solved: false,
          chapter_id: 2,
        },
        chapter3: {
          name: "chapter 3 - functions",
          question: "What is the difference between a variable and a constant?",
          answer: "A variable can be changed, a constant cannot.",
          solved: false,
          chapter_id: 3,
        },
        chapter4: {
          name: "chapter 4 - functions",
          question: "What is the difference between a variable and a constant?",
          answer: "A variable can be changed, a constant cannot.",
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
        console.log("thats", questions);
        if (req.query.loggedin == "true") {
          return res.render("dash", { id, name, questions });
        } else {
          return res.render("dash", { id, name, questions });
        }
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

app.listen(PORT, () => {
  console.log(`Server is running on port http://localhost:${PORT}/`);
});
