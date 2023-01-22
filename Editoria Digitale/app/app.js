const express = require("express")
const app = express()
const PORT = 8080 || process.env.PORT

app.set('view engine', 'hbs')

app.use(express.urlencoded({ extended: true }))
app.use(express.json())

app.get("/", (req, res) => {
    res.send("Hello World")
})

app.listen(PORT, () => {
    console.log(`Server is running on port http://localhost:${PORT}/`)
})  