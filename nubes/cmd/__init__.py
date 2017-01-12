import argparse

from nubes import dispatcher


def main():
    parser = argparse.ArgumentParser(description='Universal IaaS CLI')
    parser.add_argument('connector', help='IaaS Name')
    parser.add_argument('resource', help='Resource to perform action')
    parser.add_argument('action', help='Action to perform on resource')
    parser.add_argument('--auth-url')
    parser.add_argument('--username')
    parser.add_argument('--password')
    parser.add_argument('--project-name')
    args = parser.parse_args()
    dispatch = dispatcher.Dispatcher(args.connector, args.auth_url,
                                     args.username, args.password,
                                     args.project_name)
    resource = args.resource
    if args.action == 'list':
        # make plural
        resource = args.resource + 's'

    method_name = '_'.join([args.action, resource])
    result = getattr(dispatch, method_name)()
    return str(result)
