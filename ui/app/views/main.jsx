var React = require('react');
var Reflux = require('reflux');
var Router = require('react-router');
var RouteHandler = Router.RouteHandler;
var Link = Router.Link;

var accountStore = require('../stores/account');

var AccountBlock = React.createClass({
  // Sets initial state to that of accountStore, and updates our state accordingly.
  mixins: [Reflux.connect(accountStore, "account")],

  render: function() {
    return (
      <div>
        <span>Login: {this.state.account.name}</span>
      </div>
    );
  }
});

var MainView = React.createClass({
  render: function() {
    return (
      <div>
        <AccountBlock />
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
