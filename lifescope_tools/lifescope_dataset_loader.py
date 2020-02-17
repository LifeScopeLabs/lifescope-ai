# Suggested
# Conda https://www.anaconda.com/distribution/
# https://www.jetbrains.com/help/idea/jupyter-notebook-support.html

# https://coderwall.com/p/quwaxa/update-all-installed-python-packages-with-pip
# !pip install -U $(pip freeze | awk '{split($0, a, "=="); print a[1]}')


# !pip install graphql-core

from collections import OrderedDict

from graphql import graphql
from graphql.error import format_error
from graphql.type import (
    GraphQLArgument,
    GraphQLBoolean,
    GraphQLEnumType,
    GraphQLEnumValue,
    GraphQLField,
    GraphQLFloat,
    GraphQLID,
    GraphQLInputObjectField,
    GraphQLInputObjectType,
    GraphQLInt,
    GraphQLInterfaceType,
    GraphQLList,
    GraphQLNonNull,
    GraphQLObjectType,
    GraphQLScalarType,
    GraphQLSchema,
    GraphQLString,
    GraphQLUnionType,
)
from graphql.type.directives import GraphQLDirective
from graphql.utils.build_client_schema import build_client_schema
from graphql.utils.introspection_query import introspection_query

# https://github.com/graphql-python/graphql-core


#
# https://api.lifescope.io/gql-p


# https://atheros.ai/blog/graphql-introspection-and-introspection-queries
"""
HTTP Headers:

{
  "X-CSRF-Token": "XXXXXXXX",
  "Bearer":"XXXXXXXX"
}





type __Schema {
    types: [__Type!]!
    queryType: __Type!
    mutationType: __Type
    subscriptionType: __Type
    directives: [__Directive!]!
}

{
    __schema {
    directives {
    name
    description
    }
    subscriptionType {
        name
    description
    }
    types {
        name
    description
    }
    queryType {
        name
    description
    }
    mutationType {
        name
    description
    }
    queryType {
        name
    description
    }
}
}




mutation {
    eventSearch(sortField: "type") {
    id,
    connection_id_string,
    contact_interaction_type,
    hydratedContacts {
        id,
        avatar_url,
        handle,
        name,
        tagMasks{
            added,
            removed,
            source
        }
    },
    hydratedContent {
        id,
        embed_content,
        embed_format,
        embed_thumbnail,
        mimetype,
        tagMasks{
            added,
            removed,
            source
        },
        text,
        title,
        type,
        url
    },
    context,
    datetime,
    tagMasks {
        added,
        removed,
        source
    },
    type,
}
}

"""

"""
Executors
The graphql query is executed, by default, synchronously (using SyncExecutor). However the following executors are available if we want to resolve our fields in parallel:

graphql.execution.executors.asyncio.AsyncioExecutor: This executor executes the resolvers in the Python asyncio event loop.
graphql.execution.executors.gevent.GeventExecutor: This executor executes the resolvers in the Gevent event loop.
graphql.execution.executors.process.ProcessExecutor: This executor executes each resolver as a process.
graphql.execution.executors.thread.ThreadExecutor: This executor executes each resolver in a Thread.
graphql.execution.executors.sync.SyncExecutor: This executor executes each resolver synchronusly (default).

Usage
You can specify the executor to use via the executor keyword argument in the grapqhl.execution.execute function.

"""

# from graphql.execution.execute import execute

# execute(schema, ast, executor=SyncExecutor())



query = '{ hello }'

result = graphql(schema, query)

# https://docs.python.org/3/library/json.html

# https://stackabuse.com/download-files-with-python/

import requests

print('Beginning file download with requests')

url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
headers = {'user-agent': 'test-app/0.0.1'}
r = requests.get(url, headers=headers)

with open('/Users/scott/Downloads/cat3.jpg', 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)