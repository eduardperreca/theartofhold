const express = require("express")
const app = express()
const PORT = 8080 || process.env.PORT
const dotenv = require("dotenv")
const jwt = require("jsonwebtoken")
const bcrypt = require("bcrypt")
const path = require("path")
const { default: mongoose } = require('mongoose')

dotenv.config({ path: './.env' })
const publicDirectory = path.join(__dirname, './public')
app.use(express.static(publicDirectory))

app.set('view engine', 'hbs')

app.use(express.urlencoded({ extended: true }))
app.use(express.json())

app.get("/", (req, res) => {
    res.render("index")
})

app.get("/login", (req, res) => {
    res.render("login")
})

app.get("/register", (req, res) => {
    res.render("register")
})

app.listen(PORT, () => {
    console.log(`Server is running on port http://localhost:${PORT}/`)
})  