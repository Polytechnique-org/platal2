var AuthHeadExt = React.createClass({
    render: function() {
        return (
                <header>
                <h2>Authentification à un site externe</h2>
                <a href="">www.siteexterne.org</a>
                </header>
               );
    }
});

var AuthModule = React.createClass({
    render: function() {
        return (
                <article className="sheet signin-form">
                <form noValidate>
                <input id="Email" type="email" spellCheck="false" name="username" placeholder="Identifiant ou e-mail"/>
                <input id="Passwd" type="password" name="password" placeholder="Mot de passe"/>
                <input id="Submit" type="submit" name="connexion" value="connexion"/>
                <label>
                <input id="KeepConnect" type="checkbox" name="keep_connect" value="no"/>
                <span>
                Rester connecté
                </span>
                </label>
                </form>
                </article>
               );
    }
});

var AuthBlock = React.createClass({
    render: function() {
        return (
                <article className="auth-block">
                <AuthHeadExt/>
                <AuthModule/>
                </article>
               );
    }
});

var Content = React.createClass({
    render: function() {
        return (
                <main>
                <AuthBlock/>
                </main>
               );
    }
});


React.render(
        <Content/>,
        document.getElementById('MainContent')
        );
