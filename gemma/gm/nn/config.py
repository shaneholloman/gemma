# Copyright 2024 DeepMind Technologies Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Symbols needed to build new `TransformerConfig`."""

# pylint: disable=g-importing-member,unused-import,g-import-not-at-top

from etils import epy as _epy

with _epy.lazy_api_imports(globals()):
  from gemma.gm.nn._transformer import ModelInfo
  from gemma.modules import AttentionType
  from gemma.transformer import GEMMA3_ATTENTION_PATTERN
  from gemma.transformer import make_attention_layers_types
  from gemma.transformer import QueryPreAttentionNormalisation
  from gemma.transformer import TransformerConfig
