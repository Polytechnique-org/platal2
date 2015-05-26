'use strict';

var React = require('react');
var Reflux = require('reflux');
var Navigation = require('react-router').Navigation;
var mui = require('material-ui');
var Spacing = mui.Styles.Spacing;
var Colors = mui.Styles.Colors;

var quickSearchStore = require('../stores/quicksearch');
var QuickSearchActions = require('../actions.js').QuickSearchActions;


var MiniProfile = React.createClass({
  render: function() {
    var profile = this.props.profile;

    var blockStyle = {
      height: Spacing.desktopKeylineIncrement * 1.25 + 'px',
      padding: Spacing.desktopGutterMini + 'px',
      width: Spacing.desktopKeylineIncrement * 12 + 'px'
    };
    var imgSize = Spacing.desktopKeylineIncrement;
    var detailsStyle = {
      height: imgSize + 'px',
      verticalAlign: 'top',
      marginLeft: Spacing.desktopGutterMini,
      display: 'inline-block'
    };
    var promoStyle = {
      color: Colors.grey500
    };
    var imgStyle = {
      borderRadius: '50%',
      width: imgSize + 'px',
      height: imgSize + 'px',
      overflow: 'hidden',
      display: 'inline-block'
    };
    var imgBlock = '';
    if (this.props.profile.photo) {
      var imgInnerStyle = {};

      // Centering
      // If width is 150 and height is 100, we'll do:
      // - set maxHeight = 64 (thus width is 96 and properly cropped)
      // - set marginLeft = -16 (thus properly centered)
      // Here, -16 == (64 - 96) / 2 == 64 * (1 - width / height) / 2
      if (profile.photo.width > profile.photo.height) {
        var widthOverflow = imgSize * (1 - profile.photo.width / profile.photo.height) / 2;
        imgInnerStyle.maxHeight = imgSize + 'px';
        imgInnerStyle.marginLeft = widthOverflow + 'px';
      } else {
        var heightOverflow = imgSize * (1 - profile.photo.height / profile.photo.width) / 2;
        imgInnerStyle.maxWidth = imgSize + 'px';
        imgInnerStyle.marginTop = heightOverflow + 'px';
      }
      imgBlock = (
        <img src={profile.photo.raw_url} style={imgInnerStyle} />
      );
    }
    return (
      <mui.Paper style={blockStyle} rounded={false}>
        <span style={imgStyle}>
          {imgBlock}
        </span>
        <div style={detailsStyle}>
          <span>{profile.public_name}</span><br />
          <span style={promoStyle}>{profile.promo}</span>
        </div>
      </mui.Paper>
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
    this.refs.quicksearchQuery.focus();
  },

  doSearch: function() {
    var query = this.refs.quicksearchQuery.getValue();

    // First, notify the store that we're interested in the data
    this._triggerSearch(query);

    // Then, update the URL.
    this.replaceWith('search', {}, {'quick': query});

    // Finally, update the state for proper rendering in the form.
    this.setState({query: query});
  },

  render: function() {
    var rows = [];
    var loader = '';
    var results = this.state.results[this.state.query.trim()];
    if (results) {
      results.forEach(function(profile) {
        rows.push(
          <li key={profile.hrpid}>
            <MiniProfile profile={profile} />
          </li>
        );
      });
    } else if (this.state.query.trim()) {
      loader = (
        <mui.CircularProgress mode="indeterminate" size={0.3}/>
      );
    }

    var listStyles = {
      listStyleType: 'none',
      paddingLeft: 0
    };

    return (
      <div className="quicksearch">
        <mui.TextField floatingLabelText="Search..." ref="quicksearchQuery" value={this.state.query} onChange={this.doSearch} />
        <div className="quicksearch-result">
          <h3>Results</h3>
          {loader}
          <ul style={listStyles}>
            {rows}
          </ul>
        </div>
      </div>
    );
  }
});

module.exports = QuickSearchView;
