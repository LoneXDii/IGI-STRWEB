const express = require("express");
const router = express.Router();
const jwt = require('jsonwebtoken');
const dotenv = require('dotenv');
dotenv.config();
const multer = require('multer');
const containerClient = require('../config/blobStorage');
const guidCreator = require('../config/guidGenerator');

const User = require('../models/user');
const Role = require('../models/role');
const upload = multer();

router.post('/register', upload.single('image') ,async (req, res) => {
    const guid = guidCreator();
    container = await containerClient();
    let imageUrl;

    if(req.file){
        const contentType = req.file.mimetype;

        const blockBlobClient = container.getBlockBlobClient(guid);
        await blockBlobClient.upload(req.file.buffer, req.file.size, {
            blobHTTPHeaders: {
                blobContentType: contentType,
            },
        });
        imageUrl = blockBlobClient.url;
    }

    const user = new User(req.body);
    user.avatar_url = imageUrl;

    user.role = '673e3c3f4659e4d7e316cd32';
    await user.save();
    res.status(201).json({ message: 'User registered' });
});

router.post('/login', async (req, res) => {
    const { email, password } = req.body;
    console.log(email);
    const user = await User.findOne({ email }).populate('role');

    if (!user || !(await user.comparePassword(password))) {
        return res.status(401).json({ message: 'Invalid credentials' });
    }

    const token = jwt.sign(
        { 
            id: user._id,
            avatar: user.avatar_url,
            email: user.email,
            role: user.role.normalized_name
        }, 
        process.env.JWT_SECRET, 
        { expiresIn: '1h' });

    res.status(200).json({ token });
});

module.exports = router;