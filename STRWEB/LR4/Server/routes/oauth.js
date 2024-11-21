const express = require("express");
const router = express.Router();
const dotenv = require('dotenv');
dotenv.config();
const {OAuth2Client} = require('google-auth-library');
const jwt = require('jsonwebtoken');

async function getUserData(access_token){
    const response = await fetch(`https://www.googleapis.com/oauth2/v3/userinfo?access_token=${access_token}`);
    const data = await response.json();
    //console.log('data', data);
    return data;
}

router.get('/', async function(req, res, next){
    const code = req.query.code;
    try{
        const redirectUrl = 'http://127.0.0.1:3001/oauth';

        const oAuth2Client = new OAuth2Client(
            process.env.CLIENT_ID,
            process.env.CLIENT_SECRET,
            redirectUrl
        );

        const result = await oAuth2Client.getToken(code);
        await oAuth2Client.setCredentials(result.tokens);
        const user = oAuth2Client.credentials;
        const data = await getUserData(user.access_token);

        const token = jwt.sign(
            { 
                id: data.sub,
                name: data.name,
                type: 'google',
                role: 'customer',
                avatar: data.picture
            }, 
            process.env.JWT_SECRET,
            { expiresIn: '1h' });

        res.status(200).json({token: token});
    }
    catch(err){
        console.log("Google error");
        console.log(err);
        res.status(400).json(err);
    }

});

module.exports = router;