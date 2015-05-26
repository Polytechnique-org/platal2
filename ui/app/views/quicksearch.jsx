'use strict';

var React = require('react');
var Reflux = require('reflux');
var Navigation = require('react-router').Navigation;

var quickSearchStore = require('../stores/quicksearch');
var QuickSearchActions = require('../actions.js').QuickSearchActions;

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
    if (results) {
      results.forEach(function(profile) {
        rows.push(
          <tr key={profile.hrpid}>
            <td>{profile.public_name}</td>
          </tr>
        );
      });
    }

    return (
      <div className="quicksearch">
        <form>
          <input type="text" ref="quicksearchQuery" value={this.state.query} onChange={this.doSearch} placeholder="Recherche dans l'annuaire"/>
        </form>
        <div className="quicksearch-result">
          <table>
            <thead>
              <tr><th>Name</th></tr>
            </thead>
            <tbody>{rows}</tbody>
          </table>
        </div>
      </div>
    );
  }
});

module.exports = QuickSearchView;
