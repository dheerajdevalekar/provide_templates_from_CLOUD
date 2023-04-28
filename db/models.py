from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, DateTime, Boolean, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
from loguru import logger
from os import getenv, environ
from subprocess import getoutput

cdb = None
DBSession: sessionmaker = None
Base = declarative_base()


def get_session():
    if DBSession is not None:
        session = DBSession()
        return session
    else:
        return None


def init_db():
    # git_path = getenv("INSTALL_PATH")
    # environ["GIT_EXEC_PATH"]
    git_error = 'fatal: not a git repository (or any of the parent directories): .git'
    git_curr_tags = getoutput("git describe --tags HEAD")
    git_curr_branch = getoutput("git rev-parse --abbrev-ref HEAD")
    if git_curr_tags == git_error or git_curr_branch == git_error:
        environ["VERSION_NO"] = "GIT_NOT_FOUND"
        logger.warning("Git branch or tag not found")
    else:
        environ["VERSION_NO"] = f"{git_curr_branch}-{git_curr_tags}"
        logger.info(f'Current Version - {getenv("VERSION_NO")}')
    try:
        global cdb, DBSession
        config_path = getenv("CONFIG_PATH")
        cdb = create_engine(f'sqlite:///{config_path}/config.db', connect_args={'check_same_thread': False})
        # logger.debug(f"Found config_db")
        Base.metadata.create_all(cdb)
        Base.metadata.bind = cdb
        DBSession = sessionmaker(bind=cdb)
        return True
    except Exception as e:
        logger.critical(f"{e}")
        return False


class Templates(Base):
    __tablename__ = "base_templates"

    id = Column(Integer, primary_key=True)
    template_id = Column(Integer, nullable=False)
    version = Column(String, nullable=False)
    name = Column(String, nullable=False)
    class_code = Column(String, nullable=False)
    sub_class_code = Column(String, nullable=False)
    connection_param = Column(String, nullable=False, default="{}")
    extra_base_param = Column(String, nullable=False, default="{}")
    created_at = Column(DateTime, default=datetime.now)
    Zone_Settings = relationship("ZonesTemplates", back_populates="zones_")


class ZonesTemplates(Base):
    __tablename__ = "zone_templates"

    id = Column(Integer, primary_key=True)
    master_template_id = Column(Integer, ForeignKey('base_templates.template_id'))
    class_code = Column(String, nullable=False)
    sub_class_code = Column(String, nullable=False)
    measurement = Column(String, nullable=False)
    zone = Column(String, nullable=False)
    zone_name = Column(String, nullable=False)
    zone_type = Column(String, nullable=False)
    enable = Column(Boolean, nullable=False, default=False)
    interval_param = Column(String, nullable=False)
    local_storage_enable = Column(Boolean, nullable=False, default=True)
    cloud_storage_enable = Column(Boolean, nullable=False, default=True)
    rt_enable = Column(Boolean, nullable=False, default=True)
    overflow_param = Column(String, nullable=False, default="{}")
    alarm_param = Column(String, nullable=False, default="{}")
    min_value = Column(Float, nullable=False)
    max_value = Column(Float, nullable=False)
    hysteresis = Column(Float, nullable=False)
    multiplier = Column(Float, nullable=False, default=1.0)
    zone_param = Column(String, nullable=False, default="{}")
    is_writable = Column(Boolean, nullable=False, default=False)
    writable_param = Column(String, nullable=False, default="{}")
    created_dt = Column(DateTime, default=datetime.now)
    zones_ = relationship("Templates", back_populates="Zones_Table")
