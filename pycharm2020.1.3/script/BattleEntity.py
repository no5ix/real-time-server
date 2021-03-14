from typing import Union

from PuppetBindEntity import PuppetBindEntity
from core.common.RpcMethodArgs import Str, Dict
from core.common.RpcSupport import rpc_method, CLIENT_ONLY
from server_entity.ServerEntity import ServerEntity


class BattleEntity(ServerEntity):

    def __init__(self):
        super().__init__()
        # self.be_id = 0
        # self.bind_entity = None  # type: Union[PuppetBindEntity, None]

    # def set_puppet_bind_entity(self, pbe):
    #     self.bind_entity = pbe
    #     pbe.set_bind_ok()


    # def call_server_method(self, method_name, parameters):
    #     # if not gr.bind_entity:
    #     #     return
    #     # if gr.IS_RECORD_PLAY:
    #     #     return
    #     # if not self.dungeon:
    #     #     raise StandardError()
    #     # if const.PRINT_PROTO:
    #     #     if method_name not in ('move_to', 'CompMovement.get_rtt_info', 'CompLocalEntityRouter.route', 'ride_move_to'):
    #     #         if gr.is_client:
    #     #             gr.logger.warn("[aoi c=>s]: %s", method_name)
    #
    #     # gr.bind_entity.call_server_method(
    #     self.bind_entity.call_server_method(
    #         'battle_entity_message',
    #         # {'m': RpcIndexer.send_rpc_index(method_name), 'p': parameters}
    #         {'m': method_name, 'p': parameters}
    #     )
    #
    # # def call_client_method(self, method_name, parameters):
    # #     # if not gr.bind_entity:
    # #     #     return
    # #     # if gr.IS_RECORD_PLAY:
    # #     #     return
    # #     # if not self.dungeon:
    # #     #     raise StandardError()
    # #     # if const.PRINT_PROTO:
    # #     #     if method_name not in ('move_to', 'CompMovement.get_rtt_info', 'CompLocalEntityRouter.route', 'ride_move_to'):
    # #     #         if gr.is_client:
    # #     #             gr.logger.warn("[aoi c=>s]: %s", method_name)
    # #
    # #     # gr.bind_entity.call_server_method(
    # #     self.bind_entity.call_client_method(
    # #         'battle_entity_message',
    # #         # {'m': RpcIndexer.send_rpc_index(method_name), 'p': parameters}
    # #         {'m': method_name, 'p': parameters}
    # #     )

    @rpc_method(CLIENT_ONLY, (Str('m'), Dict('p')))
    def battle_entity_message(self, method_name, parameters):
        # try:
        #     method_name = RpcIndexer.INDEX2RPC[method_name]
        # except KeyError:
        #     self.logger.error('Failed to decode method_name for uid=%s index=%s', self.uid, method_name)
        #     return
        # puppet = self._puppet
        # if not puppet:
        #     # self.logger.error('Failed to get puppet, method_name=%s', method_name)
        #     print('Failed to get puppet, method_name=%s', method_name)
        #     return
        method_list = method_name.split('.')
        if len(method_list) == 1:
            ent = self
            name = method_name
        else:
            ent = self.get_component(method_list[0])
            name = method_list[1]
        method = getattr(ent, name, None)
        if method:
            # optimized after tick，降低客户端延迟，不然需要等下一次tick才做统计
            # if puppet.delay_calls:
            #     puppet.delay_calls.callback('opt-at', 0.001, puppet.flush_aoi_data)
            # method(ent, parameters)
            method(parameters)