from __future__ import annotations

from typing import TYPE_CHECKING

from .. import _utils

if TYPE_CHECKING:
    from anndata import AnnData

def yomix(
    adata: AnnData,
):
    import yomix
    yomix.server.start_server(adata)
