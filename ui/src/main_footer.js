var MainFooter = React.createClass({
    render: function() {
        return (
                <ul id="FooterList">
                <li>
                <a href="">À propos de polytechnique.org</a>
                </li>
                <li>
                <a href="">Aide</a>
                </li>
                </ul>
               );
    }
});

React.render(
        <MainFooter/>,
        document.getElementById('MainFooter')
        );
