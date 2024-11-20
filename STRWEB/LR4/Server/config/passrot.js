const { Strategy, ExtractJwt } = require('passport-jwt');
const User = require('../models/user');

const opts = {
    jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
    secretOrKey: 'secret',
};

module.exports = (passport) => {
    passport.use(new Strategy(opts, async (jwt_payload, done) => {
        try {
            const user = await User.findById(jwt_payload.id).populate('role').populate('doctor');
            if (user) {
                return done(null, user);
            }
            return done(null, false);
        } catch (err) {
            return done(err, false);
        }
    }));
};