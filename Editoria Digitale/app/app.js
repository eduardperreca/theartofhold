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
          return res.status(200).redirect("/?loggedin=true");
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
      const refId = Math.floor(Math.random() * 100000000000000000);
      const salt = await bcrypt.genSalt(10);
      const hashedPassword = await bcrypt.hash(password, salt);
      user = new User({
        name,
        email,
        password: hashedPassword,
        refId,
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
  if (req.cookies.token) {
    res.render("dashboard", {
      name: req.user.name,
      email: req.user.email,
      refId: req.user.refId,
      });
  } else {
    res.redirect("/login");
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on port http://localhost:${PORT}/`);
});
