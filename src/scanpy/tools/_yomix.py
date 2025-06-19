from __future__ import annotations

from typing import TYPE_CHECKING

from .. import _utils

if TYPE_CHECKING:
    from anndata import AnnData

def yomix(
    adata: AnnData,
):
    import yomix
    import nest_asyncio
    nest_asyncio.apply()
    yomix.server.start_server(adata)

    # from tornado.ioloop import IOLoop
    # from bokeh.application.handlers import FunctionHandler
    # from bokeh.application import Application
    # from bokeh.server.server import Server
    # from pathlib import Path
    #
    # filearg = Path("/home/perrin/work/code/yomix/yomix/example/pbmc.h5ad")
    #
    # if True:
    #     modify_doc = yomix.server.gen_modify_doc(filearg, None, "")
    #
    #     io_loop = IOLoop.current()
    #
    #     bokeh_app = Application(FunctionHandler(modify_doc))
    #
    #     server = Server({"/": bokeh_app}, io_loop=io_loop, port=5006)
    #     server.start()
    #
    #     print(f"Opening Yomix on http://localhost:{5006}/\n")
    #
    #     io_loop.add_callback(server.show, "/")
    #     io_loop.start()
    #
    # print("ok")
