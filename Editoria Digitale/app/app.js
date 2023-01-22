const express = require("express")
const app = express()
const PORT = 8080 || process.env.PORT
const dotenv = require("dotenv")
const jwt = require("jsonwebtoken")
const bcrypt = require("bcrypt")
const { default: mongoose } = require('mongoose')

dotenv.config({ path: './.env' })

app.set('view engine', 'hbs')

app.use(express.urlencoded({ extended: true }))
app.use(express.json())

app.get("/", (req, res) => {
    res.render("login")
})

app.listen(PORT, () => {
    console.log(`Server is running on port http://localhost:${PORT}/`)
})  