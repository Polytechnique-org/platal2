'use strict';

var React = require('react');
var Reflux = require('reflux');
var Navigation = require('react-router').Navigation;

var quickSearchStore = require('../stores/quicksearch');
var QuickSearchActions = require('../actions.js').QuickSearchActions;

var ProfileLine = React.createClass({
  render: function() {
    var profile = this.props.profile;
    if (profile.photo) {
      var photo = (
        <img src={profile.photo.raw_url} className='circle' />
      );
    } else {
      var photo = '';
    }
    return (
      <li className='collection-item avatar'>
        {photo}
        <span className="title">{profile.public_name}</span>
        <p>{profile.promo}</p>
      </li>
    );
  }
});

var QuickSearchView = React.createClass({
  mixins: [
    Reflux.connect(quickSearchStore, "results"),
    Navigation,
  ],

  getInitialState: function() {
    // Get the 'quick' field from the web query
    var query = this.props.query.quick || '';
    return {
      // this.state.results is set from quickSearchStore.
      query: query,
    };
  },

  _triggerSearch: function(query) {
    if (query.trim()) {
      QuickSearchActions.quickSearch.trigger(query.trim());
    };
  },

  componentDidMount: function() {
    this._triggerSearch(this.state.query);
  },

  doSearch: function() {
    var query = this.refs.quicksearchQuery.getDOMNode().value;

    // First, notify the store that we're interested in the data
    this._triggerSearch(query);

    // Then, update the URL.
    this.replaceWith('search', {}, {'quick': query});

    // Finally, update the state for proper rendering in the form.
    this.setState({query: query});
  },

  render: function() {
    var rows = [];
    var results = this.state.results[this.state.query.trim()];
    var loader = '';
    if (results) {
      results.forEach(function(profile) {
        rows.push(
          <ProfileLine key={profile.hrpid} profile={profile} />
        );
      });
    } else if (this.state.query.trim()) {
      // Request sent, no response yet
      loader = (
        <div className="progress">
          <div className="indeterminate"></div>
        </div>
      );
    }

    return (
      <div>
        <div className="quicksearch row">
          <form>
            <div className="input-field col s6">
              <input type="search" id="search" ref="quicksearchQuery" value={this.state.query} onChange={this.doSearch} />
              <label htmlFor='search'>Search:</label>
            </div>
          </form>
        </div>
        <div className="row">
          <div className="quicksearch-result">
            <h5>Results</h5>
            {loader}
            <ul className="collection">
              {rows}
            </ul>
          </div>
        </div>
      </div>
    );
  }
});

module.exports = QuickSearchView;
