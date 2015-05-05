/** @jsx React.DOM */
'use strict';

var React = require('react');
var MyView = require('./view.jsx');
React.render(
  <MyView />,
  document.getElementById('content')
);
