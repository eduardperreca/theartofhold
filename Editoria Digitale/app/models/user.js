const mongoose = require('mongoose')

const userSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    password: { type: String, required: true },
    refId: { type: Number, required: true },
    questions: { type: Object, required: true },

},
    { collection: 'users' }
)

const User = mongoose.model('User', userSchema)

module.exports = User