'use strict';

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
    if (this.state.account.username) {
      // Logged in
      return (
        <div>
          <span>Login: {this.state.account.name} [{this.state.account.username}]</span>
        </div>
      );
    } else if (this.state.account.loading) {
      return (
        <div>
          <span>[ Loading account ... ]</span>
        </div>
      );
    } else {
      return (
        <div>
          <a href="#">Login</a>
        </div>
      );
    }
  }
});

var AppView = React.createClass({
  render: function() {
    return (
      <div>
        <header>
          <ul>
            <li><Link to="home">Home</Link></li>
            <li><Link to="search">Search</Link></li>
            <li><Link to="info">Info</Link></li>
            <li><AccountBlock /></li>
          </ul>
        </header>
        <div className="content">
        <RouteHandler/>
        </div>
      </div>
    );
  }
});

module.exports = AppView;
