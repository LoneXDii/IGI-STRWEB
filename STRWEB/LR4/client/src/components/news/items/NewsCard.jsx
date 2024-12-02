import React from 'react';
import '../News.css';

class NewsCard extends React.Component {
    render() {
        const { title, description, urlToImage, url } = this.props.article;
        return (
            <div className="news-card">
                <img src={urlToImage} alt={title} className="news-image" />
                <h3 className="news-title">{title}</h3>
                <p className="news-description">{description}</p>
                <a href={url} className="read-more">Читать далее</a>
            </div>
        );
    }
}

export default NewsCard;