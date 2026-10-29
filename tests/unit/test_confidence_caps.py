"""The mechanical confidence caps of research/source_quality_policy.md §4 (lhmuc.registry.confidence_cap)."""
from lhmuc.registry import confidence_cap

UPLOADED_PAPER = {"access": "uploaded", "source_type": "journal_article", "category": "PEER_REVIEWED"}
UPLOADED_SLIDES = {"access": "uploaded", "source_type": "workshop_talk", "category": "PRIMARY_LHMUC"}
SNIPPET = {"access": "snippet_only", "source_type": "arxiv_preprint", "category": "PEER_REVIEWED"}


def test_no_cap_for_a_refereed_text_read_in_full():
    assert confidence_cap({"status": "reported_lhmuc"}, UPLOADED_PAPER) == (None, "")
    assert confidence_cap({"status": "imported_related", "applicability": {"category": "analogous"}}, UPLOADED_PAPER)[0] is None


def test_analogous_and_design_variant_are_capped_at_medium():
    assert confidence_cap({"status": "analogous"}, UPLOADED_PAPER)[0] == "medium"
    prov = {"status": "imported_related", "applicability": {"category": "design_variant"}}
    assert confidence_cap(prov, UPLOADED_PAPER)[0] == "medium"


def test_slides_and_unread_sources_are_capped_at_medium():
    assert confidence_cap({"status": "reported_lhmuc"}, UPLOADED_SLIDES)[0] == "medium"
    assert confidence_cap({"status": "imported_related"}, SNIPPET)[0] == "medium"


def test_synthetic_is_capped_at_low_and_the_lowest_cap_wins():
    assert confidence_cap({"status": "synthetic"}, None)[0] == "low"
    assert confidence_cap({"status": "synthetic"}, UPLOADED_SLIDES)[0] == "low"
