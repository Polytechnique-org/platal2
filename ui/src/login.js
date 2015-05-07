var SignInHeader = React.createClass({
    render: function() {
        if (this.props.isexternal) {
        return (
                <header>
                <h2>Authentification à un site externe</h2>
                <a className="friend-site" href="">www.siteexterne.org</a>
                </header>
               );
        }
        return (<header>
                <h2>Le site des élèves et anciens élèves de l'École polytechnique</h2>
                <h2>Veuillez vous authentifier</h2>
                </header>);
    }
});

var SignInForm = React.createClass({
    render: function() {
        return (
                <form noValidate>
                <input id="Email" type="email" spellCheck="false" name="username" placeholder="Identifiant ou e-mail"/>
                <input id="Passwd" type="password" name="password" placeholder="Mot de passe"/>
                <input id="Submit" type="submit" name="connexion" value="connexion"/>
                <section className="signin-misc">
                <label>
                <input id="KeepConnect" type="checkbox" name="keep_connect" value="no"/>
                <span>
                Rester connecté
                </span>
                </label>
                <a>Aide</a>
                </section>
                </form>
               );
    }
});

var Content = React.createClass({
    render: function() {
        return (
                <article className="sign-in center-content">
                <SignInHeader isexternal={false} />
                <SignInForm/>
                </article>
               );
    }
});


React.render(
        <Content/>,
        document.getElementById('Main')
        );
