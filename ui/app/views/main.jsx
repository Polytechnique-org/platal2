var React = require('react');
var Router = require('react-router');
var RouteHandler = Router.RouteHandler;
var Link = Router.Link;

var MainView = React.createClass({
  render: function() {
    return (
      <div>
        <header>
          <ul>
            <li><Link to="app">Home</Link></li>
            <li><Link to="info">Info</Link></li>
          </ul>
        </header>
        <RouteHandler/>
      </div>
    );
  }
});

module.exports = MainView;
