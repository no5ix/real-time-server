# from core.EtcdSupport import ServiceNode
from __future__ import annotations

import asyncio
from asyncio import AbstractEventLoop
# from TcpServer import ev_loop
import typing


if typing.TYPE_CHECKING:
    from core.EtcdSupport import ServiceNode


is_dev_version = True


db_save_interval_sec = 8
entity_db_name = "entity_db"
entity_collection_name = "entity_collection"


bind_entity = None
is_client = False

local_ip = None
local_port = None

# 游戏服务器名
game_server_name = None
etcd_tag = None
# game_server_name = 'battle_1'

game_json_conf = None  # type: typing.Union[typing.Dict, None]
etcd_service_node = None  # type: typing.Union[ServiceNode, None]


_EV_LOOP = None  # type: typing.Union[None, AbstractEventLoop]


def get_ev_loop() -> asyncio.AbstractEventLoop:
    global _EV_LOOP
    if _EV_LOOP is None:
        try:
            _EV_LOOP = asyncio.get_running_loop()
        except RuntimeError:
            # pass  # 正常情况不可能会发生调用此get_ev_loop比server启动还要早
            _EV_LOOP = asyncio.new_event_loop()
            asyncio.set_event_loop(_EV_LOOP)
        _EV_LOOP.set_debug(is_dev_version)
    return _EV_LOOP
