# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from wechatpy.client.api.base import BaseWeChatAPI


class MerchantExpress(BaseWeChatAPI):

    def add(self, delivery_template):
        return self._post(
            'merchant/express/add',
            data={
                'delivery_template': delivery_template
            }
        )

    def delete(self, template_id):
        return self._post(
            'merchant/express/del',
            data={
                'template_id': template_id
            }
        )

    def update(self, template_id, delivery_template):
        return self._post(
            'merchant/express/update',
            data={
                'template_id': template_id,
                'delivery_template': delivery_template
            }
        )

    def get(self, template_id):
        res = self._post(
            'merchant/express/getbyid',
            data={
                'template_id': template_id
            }
        )
        return res['template_info']

    def get_all(self):
        res = self._get('merchant/express/getall')
        return res['template_info']
