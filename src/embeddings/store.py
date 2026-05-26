from dataclasses import dataclass


@dataclass
class Chunk:
    text: str
    source_id: str
    score: float = 0.0


class VectorStore:
  """Wrapper Chroma — scaffold em memória."""

  def __init__(self) -> None:
      self._chunks: list[Chunk] = []

  def add(self, text: str, source_id: str) -> None:
      self._chunks.append(Chunk(text=text, source_id=source_id))

  def similarity_search(self, query: str, k: int = 5) -> list[Chunk]:
      if not self._chunks:
          return []
      q = query.lower()
      ranked = sorted(
          self._chunks,
          key=lambda c: sum(1 for w in q.split() if w in c.text.lower()),
          reverse=True,
      )
      return ranked[:k]
