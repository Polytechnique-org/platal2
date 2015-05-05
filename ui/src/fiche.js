
var FichePhoto = React.createClass({
    render: function() {
        return (
                <article className="fiche-photo">
                <img src="photo" alt="Photo de profil"/>
                </article>
               );
    }
});

var FicheTitle = React.createClass({
    render: function() {
        return (
                <header className="fiche-title">
                <h3>Louis Vaneau</h3>
                </header>
               );
    }
});

var FicheResume = React.createClass({
    render: function() {
        return (
                <article className="fiche-resume">
                Rue Lorem, Paris
                </article>
               );
    }
});

var Content = React.createClass({
    render: function() {
        return (
                <article className="fiche">
                <FichePhoto/>
                <FicheTitle/>
                <FicheResume/>
                </article>
               );
    }
});


React.render(
        <Content/>,
        document.getElementById('MainContent')
        );
