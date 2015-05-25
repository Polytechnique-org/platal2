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
        <span>Login: {this.state.account.name}</span>
      );
    } else if (this.state.account.loading) {
      return (
        <span>[ Loading account ... ]</span>
      );
    } else {
      return (
        <a href="#">Login</a>
      );
    }
  }
});

var AppView = React.createClass({
  render: function() {
    return (
      <div>
        <nav className="light-blue lighten-2">
          <div className="nav-wrapper container">
            <ul>
              <li><Link to="home">Home</Link></li>
              <li><Link to="search">Search</Link></li>
              <li><Link to="info">Info</Link></li>
              <li className="right"><AccountBlock /></li>
            </ul>
          </div>
        </nav>
        <div className="section container">
          <div className="row">
            <div className="content col s10 offset-s1">
              <RouteHandler/>
            </div>
          </div>
        </div>
      </div>
    );
  }
});

module.exports = AppView;
