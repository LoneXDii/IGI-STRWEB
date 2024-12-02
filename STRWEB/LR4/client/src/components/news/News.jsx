import React from 'react';
import './News.css';
import Navigation from '../navigation/Navigation';
import NewsCard from './items/NewsCard';

class News extends React.Component {
    state = {
        articles: []
    };

    componentDidMount() {
        fetch('https://newsapi.org/v2/everything?language=ru&q=medicine&excludeDomains=mail.ru&apiKey=50aff5d34e9d484a828144e8ca7edf79')
            .then(response => response.json())
            .then(data => {
                this.setState({ articles: data.articles });
            });
    }

    render() {
        return (
            <div>
                <Navigation />
                <div className="news-container">
                    {this.state.articles.map(article => (
                        <NewsCard key={article.title} article={article} />
                    ))}
                </div>
            </div>
        );
    }
}

export default News;