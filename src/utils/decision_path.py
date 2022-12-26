
def get_decision_path(model, test_set, sample_id = 0):
    feature_name = test_set.columns
    test_set = test_set.values

    node_indicator = model.decision_path(test_set)
    leaf_id = model.apply(test_set)
    feature = model.tree_.feature
    threshold = model.tree_.threshold
    

    # obtain ids of the nodes `sample_id` goes through, i.e., row `sample_id`
    node_index = node_indicator.indices[
        node_indicator.indptr[sample_id] : node_indicator.indptr[sample_id + 1]
    ]

    print("Rules used to predict sample {id}:\n".format(id=sample_id))
    for node_id in node_index:
        # continue to the next node if it is a leaf node
        if leaf_id[sample_id] == node_id:
            continue

        # check if value of the split feature for sample 0 is below threshold
        if test_set[sample_id, feature[node_id]] <= threshold[node_id]:
            threshold_sign = "<="
        else:
            threshold_sign = ">"

        print(
            "decision node {node} : {feature} = {value}) "
            "{inequality} {threshold})".format(
                node=node_id,
                # sample=sample_id,
                feature=feature_name[feature[node_id]],
                value=test_set[sample_id, feature[node_id]],
                inequality=threshold_sign,
                threshold=threshold[node_id],
            )
        )