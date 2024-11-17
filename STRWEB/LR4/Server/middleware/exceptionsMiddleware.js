function errorHandlingMiddleware(err, req, res, next) {
    console.error(err.stack);
    res.status(500).json({
        message: 'An error occurred while processing your request.',
        error: err.message,
    });
}

module.exports = errorHandlingMiddleware;