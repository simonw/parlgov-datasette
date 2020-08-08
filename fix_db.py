import sys
import sqlite_utils


def configure_fts(db):
    db["cabinet"].enable_fts(["name", "description", "comment"], tokenize="porter")
    db["country"].enable_fts(["name", "name_short"])
    db["election"].enable_fts(["comment"], tokenize="porter")
    db["external_commissioner_doering"].enable_fts(
        ["comment", "portfolio", "highest_position", "person_id_source"],
        tokenize="porter",
    )
    db["external_country_iso"].enable_fts(["country", "capital"])
    db["external_party_benoit_laver"].enable_fts(["PartyName"])
    db["external_party_castles_mair"].enable_fts(["name", "name_english"])
    db["external_party_chess"].enable_fts(["name", "name_english"])
    db["external_party_cmp"].enable_fts(
        ["name", "name_english", "comment"], tokenize="porter"
    )
    db["external_party_ees"].enable_fts(["name", "name_english"])
    db["external_party_euprofiler"].enable_fts(["name"])
    db["external_party_huber_inglehart"].enable_fts(["name", "name_english"])
    db["external_party_ray"].enable_fts(["ename", "name"])
    db["info_data_source"].enable_fts(["key", "short", "full"])
    db["party"].enable_fts(
        [
            "name_short",
            "name_english",
            "name",
            "name_nonlatin",
            "description",
            "comment",
        ],
        tokenize="porter",
    )
    db["party_change"].enable_fts(["description", "comment"], tokenize="porter")
    db["politician_president"].enable_fts(
        ["person_id_source", "description", "comment"], tokenize="porter"
    )


def fix_foreign_keys(db):
    db.add_foreign_keys(
        [
            ("cabinet", "country_id", "country", "id"),
            ("cabinet", "data_source", "info_data_source", "key"),
            ("cabinet", "previous_cabinet_id", "cabinet", "id"),
            ("cabinet", "previous_parliament_election_id", "election", "id"),
            ("cabinet", "previous_ep_election_id", "election", "id"),
            ("cabinet_party", "cabinet_id", "cabinet", "id"),
            ("cabinet_party", "party_id", "party", "id"),
            ("election", "country_id", "country", "id"),
            ("election", "previous_cabinet_id", "cabinet", "id"),
            ("election", "previous_parliament_election_id", "election", "id"),
            ("election", "previous_ep_election_id", "election", "id"),
            ("election_result", "election_id", "election", "id"),
            ("election_result", "party_id", "party", "id"),
            ("election_result", "alliance_id", "election_result", "id"),
            ("election_result", "data_source", "info_data_source", "key"),
            ("external_commissioner_doering", "country_id", "country", "id"),
            ("external_commissioner_doering", "party_id", "party", "id"),
            ("external_commissioner_doering", "data_source", "info_data_source", "key"),
            ("external_commissioner_doering", "government_party", "party", "id"),
            ("external_commissioner_doering", "previous_cabinet_id", "cabinet", "id"),
            ("external_party_cmp", "country", "country", "id"),
            ("party", "country_id", "country", "id"),
            ("party", "family_id", "party_family", "id"),
            ("party_name_change", "party_id", "party", "id"),
            ("politician_president", "country_id", "country", "id"),
            ("politician_president", "party_id", "party", "id"),
            ("info_variable", "table_id", "info_table", "id"),
        ]
    )


if __name__ == "__main__":
    if not sys.argv[-1].endswith(".db"):
        print("Usage: fix_foreign_Keys.py parlgov.db")
        sys.exit(1)
    db = sqlite_utils.Database(sys.argv[-1])
    fix_foreign_keys(db)
    configure_fts(db)
