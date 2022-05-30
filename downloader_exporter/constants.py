from enum import Enum
from collections import namedtuple

from loguru import logger

TorrentStat = namedtuple('TorrentStat', ['status', 'category', 'tracker'])

class TorrentStatus(Enum):
    UNKNOWN         = '未知'
    ALLOCATING      = '分配'
    DOWNLOADING     = '下载中'
    UPLOADING       = '上传中'
    COMPLETED       = '完成'
    CHECKING        = '校验'
    ERRORED         = '错误'
    STALLED         = '等待'
    QUEUED          = '排队'
    PAUSED          = '暂停'
    MOVING          = '移动中'

    @staticmethod
    def parse_qb(state: str):
        states = {
            ('unknown'): TorrentStatus.UNKNOWN,
            ('allocating'): TorrentStatus.ALLOCATING,
            ('downloading', 'metaDL', 'forcedDL'): TorrentStatus.DOWNLOADING,
            ('uploading', 'forcedUP'): TorrentStatus.UPLOADING,
            # (): TorrentStatus.COMPLETED,
            ('checkingUP', 'checkingDL', 'checkingResumeData'): TorrentStatus.CHECKING,
            ('missingFiles', 'error'): TorrentStatus.ERRORED,
            ('stalledUP', 'stalledDL'): TorrentStatus.STALLED,
            ('queuedUP', 'allocating', 'queuedDL'): TorrentStatus.QUEUED,
            ('pausedUP', 'pausedDL'): TorrentStatus.PAUSED,
            ('moving'): TorrentStatus.MOVING,
        }
        for key, val in states.items():
            if state in key:
                return val
        logger.warning(f"qBittorrent unknown state: {state}")
        return TorrentStatus.UNKNOWN

    @staticmethod
    def parse_de(state: str):
        states = {
            # (): TorrentStatus.UNKNOWN,
            ('Allocating'): TorrentStatus.ALLOCATING,
            ('Downloading'): TorrentStatus.DOWNLOADING,
            ('Seeding'): TorrentStatus.UPLOADING,
            # (): TorrentStatus.COMPLETED,
            ('Checking'): TorrentStatus.CHECKING,
            ('Error'): TorrentStatus.ERRORED,
            # (): TorrentStatus.STALLED,
            ('Queued'): TorrentStatus.QUEUED,
            ('Paused'): TorrentStatus.PAUSED,
            ('Moving'): TorrentStatus.MOVING,
        }
        for key, val in states.items():
            if state in key:
                return val
        logger.warning(f"Deluge unknown state: {state}")
        return TorrentStatus.UNKNOWN

    @staticmethod
    def parse_tr(state: str):
        states = {
            # (): TorrentStatus.UNKNOWN,
            # (): TorrentStatus.ALLOCATING,
            ('downloading'): TorrentStatus.DOWNLOADING,
            ('seeding'): TorrentStatus.UPLOADING,
            # (): TorrentStatus.COMPLETED,
            ('checking'): TorrentStatus.CHECKING,
            # (): TorrentStatus.ERRORED,
            # (): TorrentStatus.STALLED,
            ('check pending', 'download pending', 'seed pending'): TorrentStatus.QUEUED,
            ('stopped'): TorrentStatus.PAUSED,
            # (): TorrentStatus.MOVING,
        }
        for key, val in states.items():
            if state in key:
                return val
        logger.warning(f"Transmission unknown state: {state}")
        return TorrentStatus.UNKNOWN