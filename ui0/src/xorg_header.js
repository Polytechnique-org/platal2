var MainHeader = React.createClass({
    render: function() {
        return (
                <div className="xorg_header xorg_header_private">
                <div className="header_logo">
                <h1>Polytechnique.org</h1>
                </div>
                <div className="header_search">
                <form>
                <input type="search" name="annuaire_search" placeholder="Recherche dans l'annuaire"/>
                </form>
                </div>
                <nav>
                <div>
                <div onclick="menuVisibility()">
                <svg width="32" height="32" viewBox="0 0 400 400">
                <rect x="5" y="35" rx="20" ry="20" width="390" height="80"/>
                <rect x="5" y="160" rx="20" ry="20" width="390" height="80"/>
                <rect x="5" y="285" rx="20" ry="20" width="390" height="80"/>
                </svg>
                </div>
                <aside id="Menu"></aside>
                </div>
                </nav>
                </div>
                );
    }
});

React.render(
        <MainHeader/>,
        document.getElementById('XorgHeader')
        );
