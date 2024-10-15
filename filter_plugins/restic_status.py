from ansible.errors import AnsibleFilterError

class FilterModule(object):

    def filters(self):
        return {
            'restic_status': self.restic_status
        }

    def restic_status(self, value):
        status = ''
        if 'message_type' in value:
            message_type = value['message_type']
            if message_type == 'summary':

                status += 'Files:\n'
                status += str(value['files_new']) + ' New, '
                status += str(value['files_changed']) + ' Changed, '
                status += str(value['files_unmodified']) + ' Unmodified\n'

                status += 'Dirs:\n'
                status += str(value['dirs_new']) + ' New, '
                status += str(value['dirs_changed']) + ' Changed, '
                status += str(value['dirs_unmodified']) + ' Unmodified\n'

                status += 'Blobs:\n'
                status += str(value['data_blobs']) + ' Data Blobs, '
                status += str(value['tree_blobs']) + ' Tree Blobs\n\n'

                if 'dry_run' in value and value['dry_run']:
                    status += 'Dry Run: Yes\n\n'
                if not ('dry_run' in value):
                    status += 'Dry Run: No\n\n'

                status += 'Total files processed: ' + str(value['total_files_processed']) + ', '
                status += 'Total bytes processed: ' + '{:.2f}'.format(value['total_bytes_processed']/(1024*1024)) + 'MB' + ' = ' + '{:.2f}'.format(value['total_bytes_processed']/(1024*1024*1024)) + 'GB, '
                status += 'Total duration: ' + str(round(value['total_duration'], 1)) + 's\n'
                if 'snapshot_id' in value:
                    status += 'Creating snapshot id: ' + value['snapshot_id']
                else:
                    status += 'No snapshot id created, backup is skipped'

            elif message_type == 'verbose_status':
                if 'action' in value:
                    status += value['action'] + ': ' + value['item']
            elif message_type == 'status':
                status += 'Percent done: ' + str(value['percent_done'])
            elif message_type == 'error':
                status += str(value)
            else:
                raise AnsibleFilterError(f'message_type: {message_type} not recognized')
        else:
            raise AnsibleFilterError(f'No message_type element found')

        return status
