from __future__ import absolute_import

from django.db.models import ForeignKey

__all__ = ('FlexibleForeignKey')

class FlexibleForeignKey(ForeignKey):
    def db_type(self, connection):
        rel_field = self.related_field
        if hasattr(rel_field,'get_related_db_type'):
            return rel_field.get_related_db_type(connection)

        return super(FlexibleForeignKey,self).db_type(connection)
