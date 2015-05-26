var React = require('react');
var Router = require('react-router');
var Link = Router.Link;

var XorgFooter = React.createClass({
    render: function() {
        return (
                <ul id="FooterList">
                <li><Link to="home">Home</Link></li>
                <li><Link to="search">Search</Link></li>
                <li><Link to="info">Info</Link></li>
                </ul>
               );
    }
});

module.exports = XorgFooter;
