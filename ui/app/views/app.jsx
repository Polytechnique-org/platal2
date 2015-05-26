'use strict';

var React = require('react');
var Reflux = require('reflux');
var Router = require('react-router');
var RouteHandler = Router.RouteHandler;
var Link = Router.Link;
var mui = require('material-ui');
var ThemeManager = require('material-ui/lib/styles/theme-manager')();

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
  mixins: [Router.Navigation],

  childContextTypes: {
    muiTheme: React.PropTypes.object
  },

  getChildContext: function() {
    return {
      muiTheme: ThemeManager.getCurrentTheme()
    };
  },

  onNavChange: function(e, key, payload) {
    this.transitionTo(payload.route);
  },

  render: function() {
    var menuItems = [
      {route: 'home', text: "Home"},
      {route: 'search', text: "Search"},
      {route: 'info', text: "Info"}
    ];
    return (
      <mui.AppCanvas predefinedLayout={1}>
        <mui.AppBar title="Demo" zDepth={0} />
        <mui.LeftNav menuItems={menuItems} onChange={this.onNavChange} />
        <mui.ClearFix>
          <div>
            <RouteHandler/>
          </div>
        </mui.ClearFix>
      </mui.AppCanvas>
    );
  }
});

module.exports = AppView;
