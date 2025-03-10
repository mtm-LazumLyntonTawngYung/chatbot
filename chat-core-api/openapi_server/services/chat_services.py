import connexion
from openapi_server.services.chienowa_net_service import ChienowaNetService
from openapi_server.services.gemini_service import infer_case_group
from openapi_server.variables import (BP_RATE_THRESHOLD, CASE_GROUP_THRESHOLD, responses,
                                      CHIENOWA_GPBP_SUMMARY_URL, GP_RATE_THRESHOLD)


class ChatServices:
    def get_chat_respond(self, input_msg, bot_style):
        try:
            selected_bot_type = responses[bot_style]
            case_group_data = self.get_case_group_info(0, input_msg)

            if not case_group_data:
                return selected_bot_type['NO_DATA_MSG_REPLY']

            service = ChienowaNetService()
            gpbp_result = service.get_aggregations(
                case_group_data['chienowa_id'])

            if not self.is_valid_gpbp_result(gpbp_result):
                return selected_bot_type['NO_DATA_MSG_REPLY']

            # Get top 3 GP and BP solutions
            gp_msg = self.get_solutions_message(
                gpbp_result, GP_RATE_THRESHOLD, selected_bot_type['GP_MSG_INTRO'],
                case_group_data['name'], is_good_pt=True)
            bp_msg = self.get_solutions_message(
                gpbp_result, BP_RATE_THRESHOLD, selected_bot_type['BP_MSG_INTRO'],
                is_good_pt=False)

            # If no data in both GP and BP solutions
            if not gp_msg and not bp_msg:
                return selected_bot_type['NO_DATA_MSG_REPLY']

            # Construct the final message
            ret_msg = self.construct_final_message(
                gp_msg, bp_msg, selected_bot_type['REF_URL_INTRO'])
            return ret_msg
        except Exception as error:
            raise connexion.ProblemException(500, str(error))

    def get_case_group_info(self, care_id, body):
        """Extract case group info based on provided care_id and body."""
        case_groups = infer_case_group(care_id, body)

        if not self.is_valid_case_group(case_groups):
            return None

        # Filter inferred case groups by probability threshold
        inferred_case_groups = [
            each_case for each_case in case_groups['inferences']
            if each_case['probability'] >= CASE_GROUP_THRESHOLD
        ]

        # Get the case with the highest probability
        max_prob_case = max(inferred_case_groups,
                            key=lambda x: x['probability'], default=None)
        return max_prob_case

    def get_solutions_message(self, gpbp_result, threshold, param_msg='', symbolic_name='', is_good_pt=False):
        """Get a formatted message for top solutions based on GP rate threshold."""
        filtered_solutions = self.filter_solutions_by_rate(
            gpbp_result, threshold, is_good_pt)

        # Construct the introductory part of the message
        message_intro = f'「{symbolic_name}」{param_msg}' if is_good_pt else param_msg

        # Sort solutions based on their GP rate and take the top 3
        top_solutions = sorted(
            filtered_solutions, key=lambda x: x.gprate, reverse=is_good_pt)[:3]

        if not top_solutions:
            return ''

        solutions_text = self.format_solutions(top_solutions)

        return f'{message_intro}{solutions_text}'

    def is_valid_gpbp_result(self, gpbp_result):
        """Check if GPBP result is valid."""
        return isinstance(gpbp_result, list) and gpbp_result

    def is_valid_case_group(self, case_groups):
        """Check if case groups have valid inferences."""
        return isinstance(case_groups.get('inferences'), list) and case_groups['inferences']

    def filter_solutions_by_rate(self, gpbp_result, threshold, is_good_pt):
        """Filter solutions based on GP rate."""
        if is_good_pt:
            return [solution for solution in gpbp_result if solution.gprate >= threshold]
        else:
            return [solution for solution in gpbp_result if solution.gprate <= threshold]

    def format_solutions(self, solutions):
        """Format solutions into a string representation."""
        formatted_solutions = [
            f'{index + 1}. {solution.cope}（{round(solution.gprate * 100, 2)}%）'
            for index, solution in enumerate(solutions)
        ]
        return (formatted_solutions)

    def construct_final_message(self, gp_msg, bp_msg, url_intro):
        """Construct the final response message."""
        return f'{gp_msg}{bp_msg}{url_intro}{CHIENOWA_GPBP_SUMMARY_URL}'


