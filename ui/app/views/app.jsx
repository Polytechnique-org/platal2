'use strict';

var React = require('react');
var Reflux = require('reflux');
var Router = require('react-router');
var RouteHandler = Router.RouteHandler;
var Link = Router.Link;
var mui = require('material-ui');
var ThemeManager = require('material-ui/lib/styles/theme-manager')();
var Spacing = mui.Styles.Spacing;

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

  getStyles: function() {
    var navWidth = Spacing.desktopKeylineIncrement * 3 + 'px';
    var topHeight = Spacing.desktopKeylineIncrement + 'px';
    var styles = {
      root: {
        paddingTop: topHeight,
        position: 'relative'
      },
      nav: {
        position: 'absolute',
        top: topHeight,
        width: navWidth
      },
      content: {
        marginLeft: navWidth,
        padding: Spacing.desktopGutter + 'px',
        minHeight: '800px'
      }
    };
    return styles;
  },

  render: function() {
    var menuItems = [
      {route: 'home', text: "Home"},
      {route: 'search', text: "Search"},
      {route: 'info', text: "Info"}
    ];
    var styles = this.getStyles();

    var currentItem = null;
    for (var i = menuItems.length - 1; i >= 0; i--) {
      if (this.context.router.isActive(menuItems[i].route)) {
        currentItem = i;
        break;
      }
    }

    return (
      <mui.AppCanvas predefinedLayout={1}>
        <mui.AppBar title="Demo" zDepth={0} showMenuIconButton={false} />
        <div style={styles.root}>
          <div style={styles.content}>
            <RouteHandler/>
          </div>
          <div style={styles.nav}>
            <mui.Menu
              menuItems={menuItems}
              selectedIndex={currentItem}
              onItemClick={this.onNavChange}
              />
          </div>
        </div>
      </mui.AppCanvas>
    );
  }
});

module.exports = AppView;
