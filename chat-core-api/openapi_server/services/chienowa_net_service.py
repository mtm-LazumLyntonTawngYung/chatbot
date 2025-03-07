from sqlalchemy import desc
from openapi_server.schemas.chienowa_net_schemas import WpGsGpbpSummary, WpGsGpbpSummaryManage
from openapi_server.services.db_service import ChienowaNetDbService
from openapi_server.variables import ALL_KEYWORD_TEXT


class ChienowaNetService:
    def get_aggregations(self, param_case_group_id):
        db = ChienowaNetDbService()

        with db.start_session(commit=False) as session:

            sub_query = self._build_subquery(session)

            gpbp_result = self._fetch_aggregated_results(
                session, param_case_group_id, sub_query)

        return gpbp_result

    def _build_subquery(self, session):
        """Builds the subquery to filter summary_manage_id."""
        return session.query(WpGsGpbpSummaryManage.id).filter(
            WpGsGpbpSummaryManage.summary_type == 1,
            WpGsGpbpSummaryManage.summary_status == 1
        )

    def _fetch_aggregated_results(self, session, param_case_group_id, sub_query):
        """Fetches aggregated results from wp_gs_gpbp_summary table."""
        return session.query(
            WpGsGpbpSummary.gpbp_result_meta_id,
            WpGsGpbpSummary.parent_cluster_id,
            WpGsGpbpSummary.happen,
            WpGsGpbpSummary.cope,
            WpGsGpbpSummary.gpnum,
            WpGsGpbpSummary.bpnum,
            WpGsGpbpSummary.gprate
        ).filter(
            WpGsGpbpSummary.keyword == ALL_KEYWORD_TEXT,
            WpGsGpbpSummary.summary_manage_id.in_(sub_query),
            WpGsGpbpSummary.parent_cluster_id == param_case_group_id
        ).group_by(
            WpGsGpbpSummary.gpbp_result_meta_id,
            WpGsGpbpSummary.parent_cluster_id,
            WpGsGpbpSummary.happen,
            WpGsGpbpSummary.cope,
            WpGsGpbpSummary.gpnum,
            WpGsGpbpSummary.bpnum,
            WpGsGpbpSummary.gprate
        ).order_by(desc(WpGsGpbpSummary.gprate)).all()
