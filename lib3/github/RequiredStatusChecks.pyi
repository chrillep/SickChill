from typing import Any, Dict, List

from github.GithubObject import CompletableGithubObject

class RequiredStatusChecks(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def contexts(self) -> List[str]: ...
    @property
    def strict(self) -> bool: ...
    @property
    def url(self) -> str: ...
