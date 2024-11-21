const { Strategy, ExtractJwt } = require('passport-jwt');
const User = require('../models/user');
const jwt = require('jsonwebtoken');
const dotenv = require('dotenv');
dotenv.config();

const opts = {
    jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
    secretOrKey: process.env.JWT_SECRET
};

module.exports = (passport) => {
    passport.use(new Strategy(opts, async (jwt_payload, done) => {
        try {
            if (jwt_payload.type === 'google'){
                var gUser = {
                    _id: jwt_payload.id,
                    email: jwt_payload.name,
                    role: {normalized_name: jwt_payload.role},
                    avatar_url: jwt_payload.avatar
                };
                return done(null, gUser);
            }
            else{
                const user = await User.findById(jwt_payload.id).populate('role').populate('doctor');
                if (user) {
                    return done(null, user);
                }
            }
            return done(null, false);
        } catch (err) {
            return done(err, false);
        }
    }));
};