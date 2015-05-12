'use strict';

// Global imports
var React = require('react');
var Router = require('react-router');

// Routing
var routes = require('./routes.jsx');

Router.run(routes, Router.HistoryLocation, function(Handler) {
  React.render(<Handler/>, document.getElementById('content'));
});
