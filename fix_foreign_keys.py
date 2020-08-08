import sys
import sqlite_utils


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
    fix_foreign_keys(sqlite_utils.Database(sys.argv[-1]))
