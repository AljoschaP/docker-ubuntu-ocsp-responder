<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='utf-8'>
<meta content='GitLab Community Edition' name='description'>
<title>

GitLab
</title>
<link href="/assets/favicon-d6aa61c7c265900a7d4c45d3ac2b461f.ico" rel="shortcut icon" type="image/vnd.microsoft.icon" />
<link href="/assets/application-715bc4efac6b42deb84d495309f19f9a.css" media="all" rel="stylesheet" />
<link href="/assets/print-8597f8b497e02f892aa5a4b25d5a857b.css" media="print" rel="stylesheet" />
<script src="/assets/application-5ec1aeb4604cbfbeff836f956308b0ed.js"></script>
<meta content="authenticity_token" name="csrf-param" />
<meta content="ZMKs7PxNrqFe5medrdhUiu8JISSX32/H9mb/wlm+cAs=" name="csrf-token" />
<script type="text/javascript">
//<![CDATA[
window.gon={};gon.default_issues_tracker="gitlab";gon.api_version="v3";gon.relative_url_root="";gon.default_avatar_url="http://git01-ifm-min.ad.fh-bielefeld.de/assets/no_avatar-fd406ccede8cb1881f20921c8bfa169b.png";
//]]>
</script>
<meta content='width=device-width, initial-scale=1, maximum-scale=1' name='viewport'>
<meta content='#474D57' name='theme-color'>


</head>

<body class='ui_mars login-page application'>

<header class='navbar navbar-fixed-top navbar-gitlab'>
<div class='navbar-inner'>
<div class='container'>
<div class='app_logo'>
<a class="home" href="/explore"><img alt="Logo white" src="/assets/logo-white-0b53cd4ea06811d79b3acd486384e047.png" />
</a></div>
<h1 class='title'></h1>
<button class='navbar-toggle' data-target='.navbar-collapse' data-toggle='collapse' type='button'>
<span class='sr-only'>Toggle navigation</span>
<i class='fa fa-bars'></i>
</button>
</div>
</div>
</header>


<div class='container navless-container'>
<div class='content'>
<div class='flash-container'>
<div class='flash-alert'>
You need to sign in before continuing.
</div>
</div>

<div class='row prepend-top-20'>
<div class='col-sm-5 pull-right'>
<div>
<div class='login-box'>
<div class='login-heading'>
<h3>Sign in</h3>
</div>
<div class='login-body'>
<ul class='nav nav-tabs'>
<li class='active'>
<a data-toggle="tab" href="#tab-ldapmain">LDAP</a>
</li>
<li>
<a data-toggle="tab" href="#tab-signin">Standard</a>
</li>
</ul>
<div class='tab-content'>
<div class='active tab-pane' id='tab-ldapmain'>
<form accept-charset="UTF-8" action="/users/auth/ldapmain/callback" id="new_ldap_user" method="post"><div style="display:none"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="ZMKs7PxNrqFe5medrdhUiu8JISSX32/H9mb/wlm+cAs=" /></div>
<input autofocus="autofocus" class="form-control top" id="username" name="username" placeholder="LDAP Login" type="text" />
<input class="form-control bottom" id="password" name="password" placeholder="Password" type="password" />
<button class="btn-save btn" name="button" type="submit">LDAP Sign in</button>
</form>


</div>
<div class='tab-pane' id='tab-signin'>
<form accept-charset="UTF-8" action="/users/sign_in" class="new_user" id="new_user" method="post"><div style="display:none"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="ZMKs7PxNrqFe5medrdhUiu8JISSX32/H9mb/wlm+cAs=" /></div><input autofocus="autofocus" class="form-control top" id="user_login" name="user[login]" placeholder="Username or Email" type="text" />
<input class="form-control bottom" id="user_password" name="user[password]" placeholder="Password" type="password" />
<div class='remember-me checkbox'>
<label for='user_remember_me'>
<input name="user[remember_me]" type="hidden" value="0" /><input id="user_remember_me" name="user[remember_me]" type="checkbox" value="1" />
<span>Remember me</span>
</label>
<div class='pull-right'>
<a href="/users/password/new">Forgot your password?</a>
</div>
</div>
<div>
<input class="btn btn-save" name="commit" type="submit" value="Sign in" />
</div>
</form>


</div>
</div>
</div>
</div>

</div>

</div>
<div class='col-sm-7 brand-holder pull-left'>
<h1>
GitLab Community Edition
</h1>
<h3>Open source software to collaborate on code</h3>
<p>
Manage git repositories with fine grained access controls that keep your code secure.
Perform code reviews and enhance collaboration with merge requests.
Each project can also have an issue tracker and a wiki.
</p>
<table>
<tr>
</tr>

</table>

<p>Willkommen zum SourceCodeManagement (SCM). Bitte melden sie sich mit ihren FH-weiten Benutzerdaten an.</p>

<p>Alles für die kontinuierliche Integration finden sie in der <a href="http://jks01-ifm-min.ad.fh-bielefeld.de:8080/">Jenkins-Umgebung</a></p>

<p>Alles für Bugtracking und Projektmanagement finden sie in der <a href="http://rm01-ifm-min.ad.fh-bielefeld.de/">Redmine-Umgebung</a></p>

<p>Informationen und Hilfe zu allen Umgebungen finden sie im <a href="http://rm01-ifm-min.ad.fh-bielefeld.de/projects/sesproject">SES Projekt</a></p>

</div>
</div>
</div>
</div>
<hr>
<div class='container'>
<div class='footer-links'>
<a href="/explore">Explore</a>
<a href="http://doc.gitlab.com/" rel="nofollow">Documentation</a>
<a href="https://about.gitlab.com/" rel="nofollow">About GitLab</a>
</div>
</div>
</body>
</html>
