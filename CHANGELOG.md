# CHANGELOG

## v0.7.0 (2024-07-25)

### Feature

* feat: __logger__ (#26)

* feat: __logger__

Implements package logger, as specified in readme.

closes #21

* fix: __310_support__

* fix: __more_310_support__

* docs: __v0.7.0-rc.1__

---------

Co-authored-by: github-actions &lt;action@github.com&gt; ([`e1b6612`](https://github.com/dan1hc/fqr/commit/e1b6612b289ee9096a6109af8344dcddbfc5ed4f))

## v0.6.0 (2024-07-25)

### Feature

* feat: __make_str_generic__ (#25)

* feat: __make_str_generic__

Makes `string[Any]` more robust.

closes #22

* fix: __class_as_dict_should_be_Final__

* fix: __class_as_dict_should_be_Final__

* fix: __properly_hint_string_generic__

* fix: __properly_hint_string_generic_w_more_sys_support__

* fix: __properly_hint_string_generic_w_more_version_support__

* docs: __v0.6.0-rc.1__

* fix: __properly_hint_string_generic_cleanup__

* docs: __v0.6.0-rc.2__

---------

Co-authored-by: github-actions &lt;action@github.com&gt; ([`ca100dc`](https://github.com/dan1hc/fqr/commit/ca100dc63da2c6e54f3c9874d8846bde2a9f0145))

## v0.5.1 (2024-07-24)

### Fix

* fix: __fix_docs__ (#24)

* fix: __fix_docs__

* docs: __v0.5.1-rc.1__

---------

Co-authored-by: github-actions &lt;action@github.com&gt; ([`cde6cad`](https://github.com/dan1hc/fqr/commit/cde6cad659c5bc9f6975953fcb658fe066915926))

## v0.5.0 (2024-07-24)

### Feature

* feat: __fields_and_objs__ (#20)

* feat: __fields_and_objs__

Implements `fqr.Field` and `fqr.Object`. Still need to expand test suite to cover `fqr/objects` dir.

close #15

* docs: __v0.5.0-rc.1__

* fix: __inefficient_regex__

* docs: __v0.5.0-rc.2__

* style: __cfg_not_cns__

* refactor: __consolidate_typ__

* refactor: __error_ref_exc_for_fields__

* refactor: __mypy_11_compliance__

* docs: __v0.5.0-rc.3__

* test: __finish_obj_tests__

* docs: __v0.5.0-rc.4__

---------

Co-authored-by: github-actions &lt;action@github.com&gt; ([`56b59df`](https://github.com/dan1hc/fqr/commit/56b59dff3203ac9eb6a9e09ebd28b35a4981010e))

## v0.4.0 (2024-07-18)

### Ci

* ci: __allow_non_dunder_commits__ (#18)

Allows for non-dunder subject lines in commit messages.

closes #10 ([`79dd660`](https://github.com/dan1hc/fqr/commit/79dd6604db9c242d5c1a8954d7f83d8b3dad6ebf))

### Feature

* feat: __typed_objs__ (#19)

* feat: __typed_objs__

Implement codec for `TypedDict`, `dataclasses`, `pydantic.BaseModel`, etc. Also adds functionality for handling [read: ignoring] wrapper types (`Annotated | ClassVar | Final | InitVar`).

closes #11, closes #12

* docs: __v0.4.0-rc.1__

---------

Co-authored-by: github-actions &lt;action@github.com&gt; ([`124da16`](https://github.com/dan1hc/fqr/commit/124da1632705a4ad1b2c6362b9a0fc1204729ff8))

## v0.3.0 (2024-07-15)

### Feature

* feat: __dates_and_literals__ (#16)

* feat: __dates_and_literals__

Support dates, datetimes, and literals.

closes #9

* docs: __v0.3.0-rc.1__

---------

Co-authored-by: github-actions &lt;action@github.com&gt; ([`616eb21`](https://github.com/dan1hc/fqr/commit/616eb21c382a8761e7a0a9a1ad278d41be26b7fd))

## v0.2.0 (2024-07-15)

### Ci

* ci: __issue_templates__

* ci: __issue_templates__

* ci: __remove_legacy_issue_templates__

* docs: __v0.1.0-rc.1__

---------

Co-authored-by: github-actions &lt;action@github.com&gt; ([`02988ce`](https://github.com/dan1hc/fqr/commit/02988ced9fd9714b7af93627eb6f90db7a150ea6))

### Feature

* feat: __serializations__ (#7)

* feat: __serializations__

Adds serialization and other functionality.

close #4

* test: __improve_ci__

* test: __better_testing__

* ci: __coverage_term_report__

* test: __avoid_cov__

* test: __more_cov__

* test: __fixing_cov__

* docs: __v0.2.0-rc.1__

* test: __use_no_cover__

* ci: __better_ci__

* docs: __v0.2.0-rc.2__

* ci: __more_better_ci__

* ci: __old_ci_better_for_now__

* ci: __old_better_ci__

* perf: __regex_perf__

* docs: __v0.2.0-rc.3__

* perf: __more_regex_perf__

* docs: __v0.2.0-rc.4__

* perf: __regex_constraints__

* docs: __v0.2.0-rc.5__

* perf: __regex_constraints_ii__

* docs: __v0.2.0-rc.6__

---------

Co-authored-by: github-actions &lt;action@github.com&gt; ([`95a14eb`](https://github.com/dan1hc/fqr/commit/95a14ebc48c61cd5db0709b5610e213d419b842c))

### Unknown

* Merge branch &#39;main&#39; of github.com:dan1hc/fqr into main ([`19ba601`](https://github.com/dan1hc/fqr/commit/19ba601c886c2994e64bc1f74a49ebc032a7860d))

## v0.1.0 (2024-07-08)

### Ci

* ci: __docs_ci_fix__ ([`96e895c`](https://github.com/dan1hc/fqr/commit/96e895c10e09e488791be5b9ec7668223fad3e31))

### Feature

* feat: __init__

Scaffold the project. Include some basic functionality.

closes #1 ([`db43155`](https://github.com/dan1hc/fqr/commit/db43155ed563bb25e1dd0f23f713e53cfa932a8e))
