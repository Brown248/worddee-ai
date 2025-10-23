"""
Utility functions and helpers
"""
from .ephemeral_store import EphemeralStore

# Singleton instance
ephemeral_store = EphemeralStore()

__all__ = ['ephemeral_store', 'EphemeralStore']