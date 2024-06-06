# Comment réduire les risques d'imports circulaires ? Découper son projet

Une manière de réduire les risques d'imports circulaire dans son projet Wagtail, 
c'est de suivre les bonnes pratiques Django: diviser son projet à l'aide
d'applications django à la responsabilité très ciblée.

Dans cet exemple, `blog` et `comments` sont deux apps séparées répondant à deux
responsabilités distinctes. On peut avoir un blog sans commentaires. On peut vouloir
dans un autre projet commenter d'autres choses qu'un article de blog.

Le fait de découper évite ici l'import circulaire entre `example.comments.forms` et 
`example.blog.models`.